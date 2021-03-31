class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        zipped = zip(coefs, words)
        result = 0

        for key, value in zipped:
            result += key * len(value)

        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        enumerated = enumerate(words, start=0)
        result = 0

        for index, value in enumerated:
            result += coefs[index] * len(value)

        return result


#
# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# Evaluator.zip_evaluate(coefs, words)


words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.enumerate_evaluate(coefs, words)



