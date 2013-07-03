<h1>Open311-Inquiry</h1>
<p>
Open311 is a form of technology that provides open channels of communication for issues that concern public space and public services. Primarily, Open311 refers to a standardized protocol for location-based collaborative issue-tracking.   Open311 provides access to Services, Facilities, and Frequently Asked Questions (FAQs).  Open311 also provides the 311 Today feed which provides daily status messages regarding Public Schools, Alternate Side Parking, and Garbage/Recycling pick up. Important City announcements based on current events may also be provided through this feed.  
</p>


<b>To use the included Python Library, you must first import it:</b><br />
<code>import open311SNSL</code>

If the library fails to import, make sure python is set to search the directory that the file is located in. Then restart python and try again.



<b>Creating a open311 ServiceList object and setting the API Key/ID:</b><br />
<code>myobj = open311SNSL.servicelist('API ID' , 'API Key') </code>


<b>Changing the API Key or ID for a servicelist object that was already created: </b><br />
<code>
ServListObj.setID('NewID')<br />
ServLisObj.setKey('NewKey')
</code>


<b>Getting the API Key or ID for a DOT object that was already created: </b><br />
<code>
ServListObj.getID() <br />
ServListObj.getKey()
</code>


<b> Using an already created object, search for "all" service lists and output as a JSON or XML</b><br />
<code>
ServListObj.getServiceList(ServListObj.s_all , ServListObj.json)
</code><br />
<b>OR</b><br />
<code>
ServListObj.getServiceList(ServListObj.s_all , ServListObj.xml)
</code>




<b>For further documentation and examples, see the integrated help Doc in python:</b><br />
<code>help(DOT) </code>







