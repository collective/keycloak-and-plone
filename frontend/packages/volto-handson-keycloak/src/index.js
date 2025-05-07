const applyConfig = (config) => {
  config.settings.isMultilingual = false;
  config.settings.supportedLanguages = ['en'];
  config.settings.defaultLanguage = 'en';

  config.settings.showPloneLogin = true;

  return config;
};

export default applyConfig;
