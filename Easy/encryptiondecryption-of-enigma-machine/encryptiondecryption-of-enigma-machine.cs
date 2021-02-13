using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        string operation = Console.ReadLine();
        int pseudoRandomNumber = int.Parse(Console.ReadLine());
        List<string> rotors = new List<string>();
        for (int i = 0; i < 3; i++)
        {
            rotors.Add(Console.ReadLine());
        }
        string message = Console.ReadLine();
        string m = "";
        string m2= "";

        if(operation.Equals("ENCODE"))
        {
            for(int i=0; i<message.Count(); i++)
            {
                m+= (char) (((int)message[i]+i+pseudoRandomNumber-65)%26+65);
            }
            rotors.ForEach(rot=>{
                for(int i=0; i<m.Count(); i++)
                {
                    m2+=rot[(int)m[i]-65];
                }
                m=m2;
                m2="";
            });
            
        }
        else
        {
            rotors.Reverse();
            rotors.ForEach(rot=>{
                for(int i=0; i<message.Count(); i++)
                {
                    m2+=(char) (rot.IndexOf(message[i])+65);
                }
                message=m2;
                m2="";
            });

            for(int i=0; i<message.Count(); i++)
            {
                int temp = (int)message[i]-i-pseudoRandomNumber-65;
                while(temp<0)temp+=26;
                m+=(char)(temp+65);
            }
        }
        Console.WriteLine(m);
    }
}
