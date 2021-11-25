using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class changeBallColor : MonoBehaviour
{
    


    void OnCollisionEnter(Collision hit)
    {

        // float maxSpeed = 1.0f;

//change size
        if (hit.gameObject.transform.localScale != new Vector3(2, 2, 2))
        {
            hit.gameObject.transform.localScale = new Vector3(2, 2, 2);

        }

else
        {
            hit.gameObject.transform.localScale = new Vector3(1, 1, 1);
        }
       

       Color currentColor = hit.gameObject.GetComponent<Renderer>().material.color;
       if (currentColor == Color.black)
        {
            currentColor = Color.green;
        }
        else
        {
            currentColor = Color.black;
        }
        hit.gameObject.GetComponent<Renderer>().material.color = currentColor;

        // hit.rigidbody.AddForce(transform.forward * 40);

        Vector3 currentVelocity = hit.rigidbody.velocity;
        Vector3 highVelocity= new Vector3(0, 15, 0);
        Vector3 lowVelocity= new Vector3(0, 8, 0);
        if (hit.rigidbody.velocity == currentVelocity)
        {
            currentVelocity = highVelocity;

        }

        else
        {
            currentVelocity = lowVelocity;
        }

        //hit.rigidbody.velocity = currentVelocity;
        //hit.velocity.magnitude = 20;

        //  if (hit.relativeVelocity.magnitude < 10)
        //  {
        //     hit.relativeVelocity.magnitude = 20;

        // }

        // else
        // {
        //    hit.relativeVelocity.magnitude = 9;

        //}
        //audioSource.Play();

        //hit.gameObject.name.velocity = new Vector3(0, 10, 0);

        //hit.gameObject.GetComponent<Renderer>().velocity = new Vector3(0, 10, 0);

        //GetComponent<Rigidbody>().velocity = new Vector3(0, 10, 0);

        // rb.velocity = vel.normalized * maxSpeed;
        // hit.gameObject.GetComponent<Renderer>().velocity.magnitude= vel.normalized * maxSpeed;
        //.gameObject.GetComponent<Renderer>().velocity = new Vector2(40, 0);
    }
}
