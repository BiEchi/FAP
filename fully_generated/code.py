def segment_from_background(image: np.ndarray, threshold: int = 10) -> np.ndarray:
    """
    Description: segment the brick stack from the background
    Input: 
        -- image: the image to be segmented
        -- threshold: the threshold for the segmentation
    Output: the segmented image
    Constraints:
        -- the image is of size [640, 640]
    """
    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Threshold the image
    ret, image_threshold = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    # Find the contours of the image
    contours, hierarchy = cv2.findContours(image_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    # Draw the largest contour on the image
    image_contour = cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
    # Return the contour image
    return image_contour
    
def canny_edge_detection(segmented_image: np.ndarray) -> np.ndarray:
    """
    Description: use the canny algorithm to detect the edges of each brick
    Input: 
        -- segmented_image: the segmented image
    Output: the image with the edges detected
    Constraints:
        -- the image is of size [640, 640]
    """
    # Convert the image to grayscale
    image_gray = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)
    # Detect the edges of the image
    edges = cv2.Canny(image_gray, 100, 200)
    # Return the edges image
    return edges


def find_boundary(segmented_image: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """
    Description: find the boundary of each brick in the stack
    Input: 
        -- segmented_image: the segmented image
        -- edges: the edges in the image
    Output: the contour of the bricks in the stack
    Constraints:
        -- the image is of size [640, 640]
    """
    # Find the contours of the image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    # Draw the largest contour on the image
    image_contour = cv2.drawContours(segmented_image, [largest_contour], -1, (0, 255, 0), 2)
    # Return the contour image
    return image_contour


def detect_boundary(segmented_image: np.ndarray) -> np.ndarray:
    """
    Description: wrap canny_edge_detection and find_boundary
    """
    # Detect the edges of the image
    edges = canny_edge_detection(segmented_image)
    # Find the boundary of the image
    contour = find_boundary(segmented_image, edges)
    # Return the contour image
    return contour


def count_connected_components(contour: np.ndarray, image: np.ndarray) -> int:
    """
    Description: count the number of connected components according to the boundary in the image
    Input: 
        -- contour: the contour of the bricks in the stack
        -- image: the image to be segmented
    Output: the number of connected components
    Constraints:
        -- the image is of size [640, 640]
    """
    # Count the number of connected components
    return len(contour)


def main(path_to_image: str) -> None:
    """
    Description: call segment_from_background, detect_boundary, and count_connected_components
    """
    # Load the image
    image = cv2.imread(path_to_image)
    # Segment the image
    segmented_image = segment_from_background(image)
    # Detect the boundary of the image
    contour = detect_boundary(segmented_image)
    # Count the number of connected components
    num_components = count_connected_components(contour, segmented_image)
    # Print the number of connected components
    print(num_components)
    # Show the segmented image
    cv2.imshow('segmented_image', segmented_image)
    # Show the contour image
    cv2.imshow('contour', contour)
    # Wait for the key to be pressed
    cv2.waitKey(0)
    # Close all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    PATH = 'IMAGE_PATH'
    main(PATH)
