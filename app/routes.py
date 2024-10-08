"""
This module provides API endpoints for image enhancement using the Real-ESRGAN model.
It includes functionality to enhance images with different scale factors (e.g., 2x, 4x)
or to improve the image quality without altering the resolution.

Endpoints:
- /enhance_image_2x: Enhances the image by 2x resolution.
- /enhance_image_4x: Enhances the image by 4x resolution.
- /enhance_image_same_size: Enhances the image without changing its resolution.
"""
from flask import request, jsonify
from app import app
from PIL import UnidentifiedImageError
from .model_loader import load_esrgan_model
from .image_enhancement import process_image_enhancement

# Load the upscaler model
upscaler = load_esrgan_model(scale=4)

# Route for 2x image enhancement
@app.route('/enhance_image_2x', methods=['POST'])
def enhance_image_2x():
    """
    API endpoint that enhances the image by 2x super resolution.

    ---
    tags:
      - Image Enhancement
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        required: true
        type: file
        description: The image file to be enhanced.
    responses:
      200:
        description: Successfully enhanced the image by 2x.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Success message indicating the enhancement completion.
                enhanced_image:
                  type: string
                  description: Base64 encoded string of the enhanced image.
      400:
        description: Bad request due to missing or invalid data.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Description of the invalid input.
      404:
        description: Image file not found.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message indicating the file was not found.
      500:
        description: Internal server error due to an unexpected failure.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message describing the server-side error.
    """
    try:
        app.logger.info("Received request to enhance image by 2x")
        if 'image' not in request.files:
            app.logger.error("No file part in the request")
            return jsonify({'status': 'error', 'message': 'No image provided'}), 400

        file = request.files['image']
        if file:
            app.logger.info(f'Received image file: {file.filename}')
        else:
            app.logger.warning('No image file found in the request.')
            return jsonify({'status': 'error', 'message': 'Image file is empty'}), 400

        if file.filename == '':
            app.logger.error("No selected file")
            return jsonify({"error": "No selected file."}), 400
        # Save the uploaded file to a temporary directory inside the enhancement function
        output_image_base64 = process_image_enhancement(file, 2, upscaler)
        app.logger.info("Image enhanced successfully")
        return jsonify({
            "message": "Image enhanced successfully.",
            "enhanced_image": output_image_base64
        }), 200

    except UnidentifiedImageError:
        app.logger.error(f"Failed to identify image at {output_image_base64}", exc_info=True)
        return jsonify({'error': f"Cannot identify image at {output_image_base64}."}), 400
    except FileNotFoundError as fnf_error:
        app.logger.error(f"File not found: {str(fnf_error)}", exc_info=True)
        return jsonify({'error': 'Image file not found.'}), 404
    except ValueError as ve:
        app.logger.error(f"ValueError: {str(ve)}", exc_info=True)
        return jsonify({'error': 'Invalid input data format.'}), 400
    except Exception as e:
        app.logger.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Route for 4x image enhancement
@app.route('/enhance_image_4x', methods=['POST'])
def enhance_image_4x():
    """
    API endpoint that enhances the image by 4x super resolution.

    ---
    tags:
      - Image Enhancement
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        required: true
        type: file
        description: The image file to be enhanced.
    responses:
      200:
        description: Successfully enhanced the image by 4x.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Success message indicating the enhancement completion.
                enhanced_image:
                  type: string
                  description: Base64 encoded string of the enhanced image.
      400:
        description: Bad request due to missing or invalid data.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Description of the invalid input.
      404:
        description: Image file not found.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message indicating the file was not found.
      500:
        description: Internal server error due to an unexpected failure.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message describing the server-side error.
    """
    try:
        app.logger.info("Received request to enhance image by 4x")
        if 'image' not in request.files:
            app.logger.error("No file part in the request")
            return jsonify({'status': 'error', 'message': 'No image provided'}), 400

        file = request.files['image']
        if file:
            app.logger.info(f'Received image file: {file.filename}')
        else:
            app.logger.warning('No image file found in the request.')
            return jsonify({'status': 'error', 'message': 'Image file is empty'}), 400

        # Save the uploaded file to a temporary directory inside the enhancement function
        output_image_base64 = process_image_enhancement(file, 4, upscaler)
        app.logger.info("Image enhanced successfully")
        return jsonify({
            "message": "Image enhanced successfully.",
            "enhanced_image": output_image_base64
        }), 200

    except UnidentifiedImageError:
        app.logger.error(f"Failed to identify image at {output_image_base64}", exc_info=True)
        return jsonify({'error': f"Cannot identify image at {output_image_base64}."}), 400
    except FileNotFoundError as fnf_error:
        app.logger.error(f"File not found: {str(fnf_error)}", exc_info=True)
        return jsonify({'error': 'Image file not found.'}), 404
    except ValueError as ve:
        app.logger.error(f"ValueError: {str(ve)}", exc_info=True)
        return jsonify({'error': 'Invalid input data format.'}), 400
    except Exception as e:
        app.logger.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Route for same-size image enhancement
@app.route('/enhance_image_same_size', methods=['POST'])
def enhance_image_same_size():
    """
    API endpoint that enhances the image without changing its resolution.

    ---
    tags:
      - Image Enhancement
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        required: true
        type: file
        description: The image file to be enhanced without altering its resolution.
    responses:
      200:
        description: Successfully enhanced the image without changing its resolution.
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Success message indicating the enhancement completion.
                enhanced_image:
                  type: string
                  description: Base64 encoded string of the enhanced image.
      400:
        description: Bad request due to missing or invalid data.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Description of the invalid input.
      404:
        description: Image file not found.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message indicating the file was not found.
      500:
        description: Internal server error due to an unexpected failure.
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Error message describing the server-side error.
    """
    try:
        app.logger.info("Received request to enhance image without changing size")
        if 'image' not in request.files:
            app.logger.error("No file part in the request")
            return jsonify({'status': 'error', 'message': 'No image provided'}), 400

        file = request.files['image']
        if file:
            app.logger.info(f'Received image file: {file.filename}')
        else:
            app.logger.warning('No image file found in the request.')
            return jsonify({'status': 'error', 'message': 'Image file is empty'}), 400

        # Save the uploaded file to a temporary directory inside the enhancement function
        output_image_base64 = process_image_enhancement(
            file, 1, upscaler
        )  # Here scale is 1 for same-size enhancement
        app.logger.info("Image enhanced successfully")
        return jsonify({
            "message": "Image enhanced successfully.",
            "enhanced_image": output_image_base64
        }), 200

    except UnidentifiedImageError:
        app.logger.error(f"Failed to identify image at {output_image_base64}", exc_info=True)
        return jsonify({'error': f"Cannot identify image at {output_image_base64}."}), 400
    except FileNotFoundError as fnf_error:
        app.logger.error(f"File not found: {str(fnf_error)}", exc_info=True)
        return jsonify({'error': 'Image file not found.'}), 404
    except ValueError as ve:
        app.logger.error(f"ValueError: {str(ve)}", exc_info=True)
        return jsonify({'error': 'Invalid input data format.'}), 400
    except Exception as e:
        app.logger.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500
