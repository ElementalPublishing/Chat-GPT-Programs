using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class FirstPersonController : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float mouseSensitivity = 2f;
    public float jumpForce = 10f;
    public float gravity = 20f;
    public float crouchHeight = 0.5f;
    public float standingHeight = 1.8f;

    private CharacterController cc;
    private Transform cameraTransform;
    private Animator animator;
    private Vector3 moveDirection;
    private bool isCrouching;
    private bool isJumping;

    void Start()
    {
        cc = GetComponent<CharacterController>();
        cameraTransform = transform.Find("First Person Camera");
        animator = GetComponent<Animator>();
        Cursor.lockState = CursorLockMode.Locked;
    }

    void Update()
    {
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        transform.Rotate(Vector3.up, mouseX);
        cameraTransform.Rotate(Vector3.right, -mouseY);

        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        moveDirection = new Vector3(horizontalInput, 0f, verticalInput);
        moveDirection = transform.TransformDirection(moveDirection);
        moveDirection *= moveSpeed;

        if (cc.isGrounded)
        {
            isJumping = false;
            animator.SetBool("Jump", false);

            if (Input.GetButtonDown("Jump"))
            {
                isJumping = true;
                animator.SetBool("Jump", true);
                moveDirection.y = jumpForce;
            }
        }

        if (Input.GetButtonDown("Crouch"))
        {
            isCrouching = !isCrouching;
            animator.SetBool("Crouch", isCrouching);
            cc.height = isCrouching ? crouchHeight : standingHeight;
        }

        moveDirection.y -= gravity * Time.deltaTime;
        cc.Move(moveDirection * Time.deltaTime);
    }
}