def give_review(self):
        review_prompt = "Möchten Sie das Spiel bewerten? [Ja (1) oder Nein (2)]: "
        star_prompt = "Wie viele Sterne geben Sie dem Spiel? (1-5): "
        thanks_message = "Wir wünschen Ihnen noch einen angenehmen Tag!"
        goodbye_message = "Bis zum nächsten Mal!"
        star_words = ["0 Sterne", "1 Stern", "2 Sterne", "3 Sterne", "4 Sterne", "5 Sterne"]
        review = input(review_prompt)
        if review.lower() == '1':
            review = input(star_prompt)
            if review.isdigit() and 0 <= int(review) <= 5:
                review = int(review)
                stars_text = star_words[review]
                review_count = [0] * len(star_words)
                review_count[review] += 1

                data = {"Bewertung": star_words, "Anzahl": review_count}
                statistic = pd.DataFrame(data)
                print(statistic.to_string(index=False, header=False))
                print(goodbye_message)
        else:
            print("Danke und auf Wiedersehen!")
