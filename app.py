import os
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simple home route to test app is running
@app.route('/')
def home():
    return jsonify({"message": "DOG MOON POT backend is running successfully!"})

    # Sample route to enter the lottery
    entries = []
    totalPotAmount = 0

    @app.route('/enter', methods=['POST'])
    def enter_lottery():
        data = request.get_json()
            wallet = data.get('wallet')
                amount_sent = data.get('amount')

                    if not wallet or not amount_sent:
                            return jsonify({"success": False, "message": "Wallet address and DOG amount required"}), 400

                                if amount_sent < 10:
                                        return jsonify({"success": False, "message": "Minimum 10 DOG required to enter"}), 400

                                            global totalPotAmount
                                                totalPotAmount += amount_sent
                                                    entries.append(wallet)

                                                        return jsonify({"success": True, "message": "You successfully entered DOG MOON POT!", "entriesCount": len(entries), "totalPotAmount": totalPotAmount})

                                                        # Route to draw winner
                                                        @app.route('/draw', methods=['POST'])
                                                        def draw_winner():
                                                            global totalPotAmount
                                                                if not entries:
                                                                        return jsonify({"success": False, "message": "No entries yet!"}), 400

                                                                            winner = random.choice(entries)
                                                                                firstPrize = totalPotAmount * 0.75
                                                                                    rollover = totalPotAmount * 0.20
                                                                                        creatorFee = totalPotAmount * 0.05

                                                                                            entries.clear()
                                                                                                totalPotAmount = rollover  # rollover goes to next pot

                                                                                                    return jsonify({
                                                                                                            "success": True,
                                                                                                                    "winner": winner,
                                                                                                                            "prizes": {
                                                                                                                                        "firstPrize": firstPrize,
                                                                                                                                                    "rollover": rollover,
                                                                                                                                                                "creatorFee": creatorFee
                                                                                                                                                                        }
                                                                                                                                                                            })

                                                                                                                                                                            if __name__ == '__main__':
                                                                                                                                                                                # Run the Flask app correctly for Heroku environment
                                                                                                                                                                                    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
                                                                                                                                                                                    