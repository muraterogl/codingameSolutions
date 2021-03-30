using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        int width = int.Parse(Console.ReadLine());
        int height = int.Parse(Console.ReadLine());
        List<string> nodes = new List<string>();
        for (int i = 0; i < height; i++)
        {
            nodes.Add(Console.ReadLine());
        }

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                if (nodes[i][j] == '0')
                {
                    List<int> output = new List<int>{j, i};

                    bool rightNotFound = true;
                    for (int k = j+1; k < width; k++)
                    {
                        if (nodes[i][k] == '0')
                        {
                            output.Add(k);
                            output.Add(i);
                            rightNotFound = false;
                            break;
                        }
                    }
                    if (rightNotFound)
                    {
                        output.Add(-1);
                        output.Add(-1);
                    }

                    bool bottomNotFound = true;
                    for (int k = i+1; k < height; k++)
                    {
                        if (nodes[k][j] == '0')
                        {
                            output.Add(j);
                            output.Add(k);
                            bottomNotFound = false;
                            break;
                        }
                    }
                    if (bottomNotFound)
                    {
                        output.Add(-1);
                        output.Add(-1);
                    }

                    Console.WriteLine(String.Join(" ", output.Select(i => i.ToString())));
                }
            }
        }
    }
}
