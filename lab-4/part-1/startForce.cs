using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class startForce : MonoBehaviour
{
    // Start is called before the first frame update
    public Vector3 StartForce;
    void Start()
    {
        Rigidbody rig = GetComponent<Rigidbody>();
        rig.AddForce(StartForce, ForceMode.Impulse);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
