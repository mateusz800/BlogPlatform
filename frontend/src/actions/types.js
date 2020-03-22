export const storyActions = {
  GET_STORY: "GET_STORY",
  GET_STORY_COUNT: "GET_STORY_COUNT",
  CHANGE_LIST_PAGE: "CHANGE_ARTICLE_LIST_PAGE",
  READ_STORY: "READ_STORY",
  GET_NEW_STORY_STATUS: "GET_NEW_STORY_STATUS",
  GET_USER_STORIES:"GET_USER_STORIES",
  RESET_CURRENT_STORY: "RESET_CURRENT_STORY"
};

export const profileActions = {
  GET_PROFILE: "GET_PROFILE",
  LOGIN: 'LOGIN',
  LOGOUT: 'LOGOUT',
  SET_UPLOADED_PHOTOT_TYPE: 'SET_UPLOADED_PHOTO_TYPE', // during changing profile settings
  LOGIN_FAILED: 'LOGIN FAILED'
};

export const mediaActions = {
  ADD_NEW_PHOTO: 'ADD_NEW_PHOTO'
}


export const photoTypes = {
  STORY_PHOTO: 'story',
  STORY_COVER_PHOTO: 'story_cover',
  PROFILE_PHOTO: 'profile',
  PROFILE_BACKGROUND_PHOTO:'profile_background'
}