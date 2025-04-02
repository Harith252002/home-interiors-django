document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("getEstimateBtn").addEventListener("click", function () {
        document.getElementById("estimateForm").classList.remove("hidden");
    });

    // Static price data
    let priceData = {
        "Kitchen": 50000,
        "Living Area": 40000,
        "Bedroom": 35000,
        "Balcony": 20000,
        "Washroom Interiors":50000,
        "Wall Decor":40000,
        "Dinning Area":70000,
        "Flooring":55000,

    };

    let quantities = { "Kitchen": 0, "Living Area": 0, "Bedroom": 0, "Balcony": 0 ,"Washroom Interiors":0,"Wall Decor":0,"Dinning Area":0,"Flooring":0};
    let totalPrice = 0;

    // **🔹 Fix: Floor Plan Selection Highlight**
    document.querySelectorAll(".floor-plan button").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelectorAll(".floor-plan button").forEach(btn => btn.classList.remove("selected"));
            this.classList.add("selected");
        });
    });

    // **🔹 Fix: Purpose Selection Highlight**
    document.querySelectorAll(".purpose button").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelectorAll(".purpose button").forEach(btn => btn.classList.remove("selected"));
            this.classList.add("selected");
        });
    });

    // Update total price function
    function updateTotalPrice() {
        totalPrice = 0;
        for (let category in quantities) {
            totalPrice += (quantities[category] * priceData[category]);
        }
        document.getElementById("totalPriceDisplay").innerText = `Total Estimate: ₹${totalPrice}`;
    }

    // Quantity buttons logic
    document.querySelectorAll(".quantity-btn").forEach(button => {
        button.addEventListener("click", function () {
            let input = this.parentElement.querySelector(".quantity-input");
            let category = input.dataset.category;
            let currentValue = parseInt(input.innerText) || 0;

            if (this.dataset.type === "increase") {
                input.innerText = currentValue + 1;
                quantities[category] += 1;
            } else if (this.dataset.type === "decrease" && currentValue > 0) {
                input.innerText = currentValue - 1;
                quantities[category] -= 1;
            }

            updateTotalPrice();
        });
    });

    // Form Navigation
    function showStep(step) {
        document.querySelectorAll(".form-step").forEach(s => s.classList.add("hidden"));
        document.getElementById("step" + step).classList.remove("hidden");

        if (step == 3) {
            updateTotalPrice();
        }
    }

    document.querySelectorAll(".next-btn").forEach(button => {
        button.addEventListener("click", function () {
            let nextStep = this.dataset.next;
            showStep(nextStep);
        });
    });

    document.querySelectorAll(".back-btn").forEach(button => {
        button.addEventListener("click", function () {
            let prevStep = this.dataset.prev;
            showStep(prevStep);
        });
    });
});