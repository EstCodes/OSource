import json
import uuid

class Quote:
    def __init__(self, quote_id, text, origin):
            self.quote_id = quote_id
            self.text = text
            self.origin = origin

    def save_quote(quote, text, origin, quote_id):
            quote.text = text 
            quote.origin = origin

            print('Save a quote')
            text = input('Text quote: ')
            origin = input('Origin quote: ')
            quote_id = str(uuid.uuid4())
            
            # Define data for Json
            data = {
                'quote_id': quote_id,
                'text': text,
                'origin': origin
            }
            filename = 'OpenSource/savequotes/quotes.json'

            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print(f"JSON data successfully written to {filename}")
            print(f"Quote saved with ID: {quote_id}")


            # POR CORREGIR - DEBE ADJUTANRSE UN LISTADO EN ESTILO JSON
            # NO SE DEBE REEMPLAZAR ANTIGUAS QUOTES
            confirm = input("Insert a new quote? (Y/N): ")
            if confirm.lower() == 'y' or confirm.lower() == 'yes' or confirm.lower() == 'sure':
                Quote.save_quote(quote, text=None, origin=None, quote_id=None)
            else:
                print("Exiting the quote saving process.")

if __name__ == "__main__":
    quote = Quote(quote_id=None, text=None, origin=None)
    Quote.save_quote(quote, quote.text, quote.origin, quote_id=None)

