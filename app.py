from flask import Flask, request
from flask_cors import CORS, cross_origin
import yake

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/extract', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def extract():
    text = request.args.get('sentence')
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.5
    deduplication_algo = 'seqm'
    window_size = 1
    num_of_keywords = 3

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                dedupFunc=deduplication_algo, windowsSize=window_size, top=num_of_keywords,
                                                features=None)
    extracted_keywords = custom_kw_extractor.extract_keywords(text)
    keywords = []
    for kw in extracted_keywords:
        keywords.append(kw[0])
    return keywords

if __name__ == '__main__':
    app.run()
