from flask import Flask, jsonify
app = Flask(__name__)

# Sample data for the lottery pot (this would be dynamic in a real system)
totalPotAmount = 1000  # This would be dynamically calculated based on user entries
rolloverAmount = 0  # Carryover amount for the next round

# Prize distribution logic
def distribute_prizes():
    # 1st Prize: 75% of the total pot
        firstPrize = totalPotAmount * 0.75

            # 2nd Prize: 10% of the rollover
                secondPrize = rolloverAmount * 0.10

                    # 3rd Prize: 10% of the rollover
                        thirdPrize = rolloverAmount * 0.10

                            # Rollover: 20% of the total pot for the next round
                                global rolloverAmount
                                    rolloverAmount = totalPotAmount * 0.20

                                        # Creator Fee: 5% of the total pot
                                            creatorFee = totalPotAmount * 0.05

                                                return {
                                                        "firstPrize": firstPrize,
                                                                "secondPrize": secondPrize,
                                                                        "thirdPrize": thirdPrize,
                                                                                "rolloverAmount": rolloverAmount,
                                                                                        "creatorFee": creatorFee
                                                                                            }

                                                                                            # Endpoint to trigger the lottery and return prize distribution
                                                                                            @app.route('/enter', methods=['POST'])
                                                                                            def enter_lottery():
                                                                                                prizes = distribute_prizes()
                                                                                                    return jsonify({
                                                                                                            "success": True,
                                                                                                                    "message": "Lottery round processed successfully",
                                                                                                                            "prizes": prizes
                                                                                                                                })

                                                                                                                                # Run the Flask app
                                                                                                                                if __name__ == '__main__':
                                                                                                                                    app.run(debug=True, host='0.0.0.0', port=3000)
                                                                                                                                    