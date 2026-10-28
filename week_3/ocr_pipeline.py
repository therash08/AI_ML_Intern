from pathlib import Path
import json
import cv2
import numpy as np
import easyocr

PROJECT_DIR = Path(__file__).resolve().parent
RAW_DIR = PROJECT_DIR / "raw_images"
CLEANED_DIR = PROJECT_DIR / "cleaned_images"
OUTPUT_DIR = PROJECT_DIR / "outputs"

CONFIDENCE_THRESHOLD = 0.60


def load_image(path):
    image_bytes = np.fromfile(str(path), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError(f"Cannot read image: {path}")

    return image


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    cleaned = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    return cleaned


def format_results(results):
    return [
        {
            "text": str(text),
            "confidence": round(float(confidence), 4),
            "bounding_box": [
                [float(x), float(y)] for x, y in bbox
            ],
            "needs_review": float(confidence) < CONFIDENCE_THRESHOLD
        }
        for bbox, text, confidence in results
    ]


def average_confidence(results):
    if not results:
        return 0.0

    return sum(float(r[2]) for r in results) / len(results) * 100


def main():
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_files = sorted([
        p for p in RAW_DIR.iterdir()
        if p.is_file()
        and p.suffix.lower() in {".jpg", ".jpeg", ".png"}
    ])

    if not 3 <= len(raw_files) <= 5:
        raise ValueError("Expected 3-5 receipt images.")

    print("Initializing EasyOCR...")
    reader = easyocr.Reader(["en"], gpu=False)

    report = {
        "project": "Automated Invoice & Receipt Digitization",
        "ocr_engine": "EasyOCR",
        "confidence_threshold": CONFIDENCE_THRESHOLD,
        "total_receipts": len(raw_files),
        "receipts": []
    }

    for index, raw_path in enumerate(raw_files, start=1):
        image = load_image(raw_path)
        cleaned_image = preprocess_image(image)

        cleaned_path = (
            CLEANED_DIR / f"receipt_{index:02d}_cleaned.png"
        )

        if not cv2.imwrite(str(cleaned_path), cleaned_image):
            raise IOError(f"Cannot save: {cleaned_path}")

        # OCR on both original and preprocessed images
        raw_results = reader.readtext(image, detail=1)
        cleaned_results = reader.readtext(cleaned_image, detail=1)

        raw_avg = average_confidence(raw_results)
        cleaned_avg = average_confidence(cleaned_results)

        # Confidence-based preference is only a heuristic
        preferred = "raw" if raw_avg >= cleaned_avg else "cleaned"
        selected_results = (
            raw_results if preferred == "raw" else cleaned_results
        )

        report["receipts"].append({
            "receipt_id": index,
            "raw_image": raw_path.name,
            "cleaned_image": cleaned_path.name,
            "raw_average_confidence": round(raw_avg, 2),
            "cleaned_average_confidence": round(cleaned_avg, 2),
            "preferred_version_by_confidence": preferred,
            "raw_ocr": format_results(raw_results),
            "cleaned_ocr": format_results(cleaned_results)
        })

        print(f"\nReceipt {index}: {raw_path.name}")
        print(f"Raw Confidence: {raw_avg:.2f}%")
        print(f"Cleaned Confidence: {cleaned_avg:.2f}%")
        print(f"Selected Version: {preferred}")
        print(f"Detected Text Regions: {len(selected_results)}")

        for _, text, confidence in selected_results:
            print(f"  {text} | Confidence: {confidence:.2%}")

    json_path = OUTPUT_DIR / "ocr_results.json"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("OCR PIPELINE COMPLETED SUCCESSFULLY!")
    print("Total Receipts:", len(report["receipts"]))
    print("JSON Output:", json_path)


if __name__ == "__main__":
    main()
