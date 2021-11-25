


using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class meshScript : MonoBehaviour
{
    private Vector3[] vertices;
    private Vector2[] uv;
    private int[] triangles;
    private Mesh mesh;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("We are debuging ........");
        mesh = new Mesh();
        int height = 40;
        int width = 40;
        int size = 4 * height * width;
        uv = new Vector2[size];
        vertices = new Vector3[size];
        triangles = new int[6 * height * width];




        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {

                vertices[(i * 40 + j) * 4 + 0] = new Vector3((float)((1.0 / 8.0) * i - 2.5), (float)((1.0 / 8.0) * j - 2.5), 0);
                vertices[(i * 40 + j) * 4 + 1] = new Vector3((float)((1.0 / 8.0) * i - 2.5), (float)((1.0 / 8.0) * (j + 1) - 2.5), 0);
                vertices[(i * 40 + j) * 4 + 2] = new Vector3((float)((1.0 / 8.0) * (i + 1) - 2.5), (float)((1.0 / 8.0) * (j + 1) - 2.5), 0);
                vertices[(i * 40 + j) * 4 + 3] = new Vector3((float)((1.0 / 8.0) * (i + 1) - 2.5), (float)((1.0 / 8.0) * j - 2.5), 0);



                triangles[(i * 40 + j) * 6 + 0] = ((i * 40 + j) * 4 + 0);
                triangles[(i * 40 + j) * 6 + 1] = ((i * 40 + j) * 4 + 1);
                triangles[(i * 40 + j) * 6 + 2] = ((i * 40 + j) * 4 + 2);
                triangles[(i * 40 + j) * 6 + 3] = ((i * 40 + j) * 4 + 0);
                triangles[(i * 40 + j) * 6 + 4] = ((i * 40 + j) * 4 + 2);
                triangles[(i * 40 + j) * 6 + 5] = ((i * 40 + j) * 4 + 3);



                uv[(i * 40 + j) * 4 + 0] = new Vector2(i * (float)(1.0 / 40), j * (float)(1.0 / 40));
                uv[(i * 40 + j) * 4 + 1] = new Vector2(i * (float)(1.0 / 40), (j + 1) * (float)(1.0 / 40));
                uv[(i * 40 + j) * 4 + 2] = new Vector2((i + 1) * (float)(1.0 / 40), (j + 1) * (float)(1.0 / 40));
                uv[(i * 40 + j) * 4 + 3] = new Vector2((i + 1) * (float)(1.0 / 40), j * (float)(1.0 / 40));


            }
        }
        mesh.Clear();
        mesh.vertices = vertices;
        mesh.uv = uv;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
        GetComponent<MeshFilter>().mesh = mesh;

    }


    void Update()
    {
        float v_height;
        int a = 2;


        for (int i = 0; i < vertices.Length; i++)
        {
            v_height = (float)(Math.Cos(Math.PI * vertices[i].x) * Math.Cos(Math.PI * vertices[i].y) * Math.Sin(a * Time.time));
            vertices[i].z = v_height;
        }
        mesh.vertices = vertices;
        mesh.RecalculateNormals();
        mesh.RecalculateBounds();
        GetComponent<MeshFilter>().mesh = mesh;
    }
}
