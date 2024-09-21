# Embedding-Based Text Similarity Program

This project demonstrates how to use **OpenAI's text embeddings** to calculate the similarity between different pieces of text. The program reads text from a file, generates embeddings for each text using OpenAI's `text-embedding-ada-002` model, and computes the cosine similarity between all pairs of embeddings. The results are displayed in a ranked order based on similarity.

## Features

- **Text Embeddings**: Uses OpenAI's API to generate vector embeddings for text using the `text-embedding-ada-002` model.
- **Cosine Similarity**: Calculates the cosine similarity between embeddings to quantify how close two pieces of text are in meaning.
- **Encoding Handling**: The program tries multiple encodings (`utf-8`, `latin-1`, `cp1252`) to handle text file reading errors.
  
## Table of Contents

- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Embeddings](#embeddings)
- [Cosine Similarity](#cosine-similarity)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bdeva1975/TextSim-Embeddings.git
   cd embedding-comparison
   ```

2. **Install dependencies**:
   ```bash
   pip install openai numpy python-dotenv
   ```

3. **Setup OpenAI API key**:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## How It Works

1. **Loading the Text**: The program reads lines of text from a file located at `<path to folder>/items.txt`, using different encodings to ensure compatibility.
   
2. **Embedding Generation**: Each line of text is passed to the `get_embedding()` function, which calls OpenAI's API to generate a 1536-dimensional vector for that text. These vectors, or **embeddings**, represent the semantic meaning of the text in a high-dimensional space.

3. **Cosine Similarity**: The similarity between embeddings is calculated using cosine similarity, which measures the angle between two vectors. Values range from `-1` (completely different) to `1` (completely similar).

4. **Ranking**: For each text, the program ranks all other texts by similarity and prints the results.

## Usage

1. **Prepare your text file**: Ensure that your text file is located at `e:/amazoncode/labs/embedding/items.txt` with each line containing a separate piece of text.

2. **Run the program**:
   ```bash
   python main.py
   ```

3. **View the output**: The program will display the closest matches for each text item, ranked by similarity score.

## Embeddings

Embeddings are dense vector representations of text that capture its semantic meaning. In this program, we use the `text-embedding-ada-002` model from OpenAI, which generates a 1536-dimensional vector for each piece of text. Embeddings are especially useful for:

- **Clustering**: Grouping similar texts together.
- **Recommendation Systems**: Recommending related content based on similarity.
- **Semantic Search**: Finding relevant information by meaning rather than keywords.

### Example of an Embedding

Given a text input like `"OpenAI's embeddings are powerful."`, the embedding might look something like:

```python
[0.021, -0.033, 0.045, ..., 0.002]  # A 1536-dimensional vector
```

These embeddings capture the essence of the text, allowing us to compare different pieces of text effectively.

## Cosine Similarity

The **cosine similarity** between two vectors measures the cosine of the angle between them. It is defined as:

\[
\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
\]

Where:
- \( A \) and \( B \) are the embeddings (vectors).
- \( \cdot \) represents the dot product.
- \( \|A\| \) and \( \|B\| \) represent the norms (magnitudes) of the vectors.

Cosine similarity ranges from `-1` to `1`:
- `1` means the vectors are identical.
- `0` means they are orthogonal (no similarity).
- `-1` means they are opposites.

### Example Output

```
Closest matches for 'Artificial Intelligence'
----------------
1.000000     Artificial Intelligence
0.943257     Machine Learning
0.892344     Deep Learning
0.678901     Robotics
...
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By leveraging OpenAI's embeddings and cosine similarity, this program provides an efficient way to measure and compare the semantic meaning of different pieces of text.
