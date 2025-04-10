import json

def prepare_dataset():
    """
    Create a dummy dataset of HVAC product descriptions with expected JSON outputs.
    Replace with your actual data preparation logic.
    """
    dataset = [
        {
            "input": "ACME SuperCool Chiller 3000: Model X100, Capacity: 5 Ton, Manufacturer: ACME Corp.",
            "output": {
                "product_name": "SuperCool Chiller 3000",
                "model_number": "X100",
                "category": "Chiller",
                "specs": "Capacity: 5 Ton",
                "manufacturer": "ACME Corp."
            }
        }
    ]
    with open("hvac_dataset.json", "w") as f:
        json.dump(dataset, f, indent=4)
    print("Dataset prepared and saved to hvac_dataset.json")

if __name__ == "__main__":
    prepare_dataset()
