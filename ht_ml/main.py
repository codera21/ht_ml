from ht_ml.constants import HTML_DIR
from ht_ml.core.datasets import Datasets
from ht_ml.core.feature_engg import preprocess_html
from sklearn.feature_extraction.text import CountVectorizer
import html_to_json
import json


def main():

    # with open(HTML_DIR / 'zZxlyF5zJQff8Dn.html', 'r') as f:
    #     html_str = f.read()
    #     a = html_to_json.convert(html_str)

    print("Its do or die situation now")
    d = Datasets()
    objs = d.read_dataset(n=5, suffle=True)

    # filter out empty html

    html_chunks = [preprocess_html(obj['html_chunk']) for obj in objs]
    a = html_to_json.convert(html_chunks[0])
    print(json.dumps(a))

    vectorizer = CountVectorizer(ngram_range=(1, 1), analyzer='word')
    X = vectorizer.fit_transform(html_chunks)
    print(vectorizer.get_feature_names_out())


if __name__ == '__main__':
    main()
