#ifndef __OBJECTCLASSLIST_H__
#define __OBJECTCLASSLIST_H__

struct ObjectDetectionItem {
    uint8_t index;
    const char* objectName;
    uint8_t filter;
};

ObjectDetectionItem itemList[1] = {
    {0,  "bird",         1},
};

#endif
