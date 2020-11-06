import pymel.core as pm
import pymel.core.datatypes as dt


def printHierarchy(node, listOfJoints):

    for childSource in node.getChildren():
		listOfJoints.append(childSource)
		if childSource.numChildren() > 0:
			printHierarchy(childSource, listOfJoints)
            
           
                      
#-------------------------------------------------------------------------

def jointList (rootName):
	try:
		root = pm.nodetypes.Joint( rootName )
	except:
		print "joint dosen't exist"
	print root
	listOfJoints = [root]
	print listOfJoints
	printHierarchy(root, listOfJoints)
	print listOfJoints
	return listOfJoints

#--------------------------------------------------------------------------

def parnatMatrix(myJoint):
	if(myJoint.getParent() != None):
		parant = myJoint.getParent()
		return  parant.getRotation().asMatrix() * parant.getOrientation().asMatrix() * parnatMatrix(parant)
	else:
		return dt.Matrix()

#---------------------------------------------------------------------------

#testListS = ['joint1', 'joint2', 'joint4', 'joint5', 'joint6', 'joint8', 'joint9','joint10', 'joint11', 'joint12']
#testListT = ['joint13', 'joint14', 'joint15', 'joint16', 'joint17', 'joint18', 'joint19', 'joint20', 'joint21', 'joint22']

def theTransferAnimation (jointListS, jointListT):
	print jointListS
	print jointListS[0]
	for i in range(0, len(jointListS)):
		pm.currentTime( 0, edit=True )
		jointS = pm.nodetypes.Joint( jointListS[i] )
		jointT = pm.nodetypes.Joint( jointListT[i] )
		
		bindPoseS = jointS.getRotation().asMatrix()
		bindPoseT = jointT.getRotation().asMatrix()
		
		parantMatrixS = parnatMatrix(jointS)
		parantMatrixT = parnatMatrix(jointT)
		
		oritationMatrixS = jointS.getOrientation().asMatrix()
		oritationMatrixT = jointT.getOrientation().asMatrix() 
		
		parantMatrixXOriantationSInv = parantMatrixS.inv() * oritationMatrixS.inv()
		parantMatrixXOriantationS = oritationMatrixS * parantMatrixS
		
		parantMatrixXOriantationTInv = parantMatrixT.inv() * oritationMatrixT.inv()
		parantMatrixXOriantationT = oritationMatrixT * parantMatrixT
		
		print parantMatrixT
		nrOfKeys = pm.keyframe( jointListS[i] , attribute='rotateY', query=True, keyframeCount=True )
		print nrOfKeys
		for j in range(0, nrOfKeys):
			curentKeyFrame = pm.keyframe(jointListS[i], query=True, index = j, attribute='rotateY', timeChange=True )
			

			pm.currentTime( curentKeyFrame[0], edit=True )
			rotationMatrix = jointS.getRotation().asMatrix()
           
			R1 = bindPoseS.inv() * rotationMatrix
			R2 = parantMatrixXOriantationSInv * R1 * parantMatrixXOriantationS
			R3 = parantMatrixXOriantationT * R2 * parantMatrixXOriantationTInv
			R4 = bindPoseT * R3
			finalRotation = pm.datatypes.EulerRotation(R4)
			
			jointT.setRotation(finalRotation)
			if(i == 0):
				jointT.setTranslation(jointS.getTranslation())
			pm.setKeyframe(jointT)




#theTransferAnimation (testListS, testListT)
