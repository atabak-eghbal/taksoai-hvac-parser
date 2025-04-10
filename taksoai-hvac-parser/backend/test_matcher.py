# backend/test_matcher.py

from app.services import matcher

def test_match_amazon():
    # Create a dummy product dictionary to simulate parsed data.
    product = {
        "product_name": "SuperCool Chiller 3000",
        "model_number": "X100"
    }
    vendor_info = matcher.match_amazon(product)
    print("Vendor Info Returned:")
    print(vendor_info)

if __name__ == "__main__":
    print("Running Product Matching Test...\n")
    test_match_amazon()
