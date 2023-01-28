string[] matrix = new string[] { "abc","ded"};

int rows = matrix.Length;
int cols = matrix[0].Length;

// Add the border of asterisks
for (int i = 0; i < rows; i++) {
    matrix[i] = "*" + matrix[i] + "*";
}

// Create the top and bottom border
string topBottom = new string('*', cols + 2);

// Add the top and bottom border to the matrix
List<string> framedMatrix = new List<string>();
framedMatrix.Add(topBottom);
framedMatrix.AddRange(matrix);
framedMatrix.Add(topBottom);

return framedMatrix.ToArray();