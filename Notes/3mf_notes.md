# 3MF Notes

## 3MF File Structure

- 3MF is a container format for 3D printing models.
- It is a zip file with a .3mf extension.
- It contains a manifest.xml file that lists the files in the package.
- All XML content is UTF-8 encoded.

## Payload

- The payload is the main content of the 3MF file and contains the 3D model data.
- The payload is typically a binary file with a .model extension.
- The payload can contain one or more 3D objects, each of which is represented by a mesh.
- The payload can also contain texture maps, materials, and other data needed to render the 3D model.

## Metadata

- The metadata is optional and contains information about the 3MF file.
- The metadata is typically stored in a .metadata file.
- The metadata can contain information such as the author, creation date, and description of the 3D model.

## 3D Models

- 3D models are represented by a mesh.
- A mesh is a collection of vertices, edges, and faces.
- Each face is a triangle, and each triangle is defined by three vertices.
- The vertices are represented by a list of 3D coordinates.
- The edges are represented by a list of indices into the vertex list.
- The faces are represented by a list of indices into the vertex list.

### Coordinate Space

- 3D models are defined in a coordinate space.
- The coordinate space is a right-handed coordinate system with the Z-axis pointing up.
- The coordinate space is defined by a bounding box.    
