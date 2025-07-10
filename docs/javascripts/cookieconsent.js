// 检查本地存储中是否已经有用户的 Cookie 同意选择 
const hasConsent = localStorage.getItem('cookieConsent');  
 
if (!hasConsent) { 
    CookieConsent.run({  
        guiOptions: { 
            consentModal: { 
                layout: "box", 
                position: "bottom left", 
                equalWeightButtons: true, 
                flipButtons: false 
            }, 
            preferencesModal: { 
                layout: "box", 
                position: "right", 
                equalWeightButtons: true, 
                flipButtons: false 
            } 
        }, 
 
        categories: { 
            necessary: { 
                enabled: true,  // this category is enabled by default 
                readOnly: true  // this category cannot be disabled 
            }, 
            analytics: { 
                services: {} 
            }, 
            chat: {}, 
            marketing: {} 
        }, 
        cookie: { domain: '.cudy.com'  }, 
        language: { 
            default: 'en', 
            translations: { 
                en: { 
                    consentModal: { 
                        title: 'We use cookies', 
                        description: 'Hi, this website uses essential cookies to ensure its proper operation and tracking cookies to understand how you interact with it. The latter will be set only after consent. <button type="button" data-cc="c-settings" class="cc-link">Let me choose</button>', 
                        acceptAllBtn: 'Accept all', 
                        acceptNecessaryBtn: 'Reject all', 
                        showPreferencesBtn: 'Manage Individual preferences' 
                    }, 
                    preferencesModal: { 
                        title: 'Cookie preferences', 
                        acceptAllBtn: 'Accept all', 
                        acceptNecessaryBtn: 'Reject all', 
                        savePreferencesBtn: 'Accept current selection', 
                        closeIconLabel: 'Close', 
                        sections: [ 
                            { 
                                title: 'Cookie usage 📢', 
                                description: 'I use cookies to ensure the basic functionalities of the website and to enhance your online experience. You can choose for each category to opt-in/out whenever you want. For more details relative to cookies and other sensitive data, please read the full <a href="/privacy-policy/" class="cc-link">privacy policy</a>.' 
                            }, 
                            { 
                                title: 'Strictly necessary cookies', 
                                description: 'These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as redirecting you to the webstore according to our location, setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.', 
 
                                //this field will generate a toggle linked to the 'necessary' category 
                                linkedCategory: 'necessary' 
                            }, 
                            { 
                                title: 'Performance and Analytics', 
                                description: 'These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.', 
                                linkedCategory: 'analytics' 
                            }, 
                            { 
                                title: 'Chat cookies', 
                                description: 'These cookies allow us provide you with a smooth customer service experience via freshchat chat and provide seamless technical support on our site.', 
                                linkedCategory: 'chat' 
                            }, 
                            { 
                                title: 'Advertisement and Targeting cookies', 
                                description: 'These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.', 
                                linkedCategory: 'marketing' 
                            }, 
                            { 
                                title: 'More information', 
                                description: 'For any queries in relation to our policy on cookies and your choices, please <a class="cc-link" href="/contacts/">contact us</a>.' 
                            } 
                        ] 
                    } 
                } 
            } 
        }, 
 
        onConsent: ({ cookie }) => { 
            // 当用户做出选择后，将选择结果存储到本地存储中 
            localStorage.setItem('cookieConsent',  JSON.stringify(cookie));  
            gtag('consent', 'update', { 
                'ad_storage': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'ad_user_data': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'ad_personalization': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'analytics_storage': cookie.categories.includes('analytics')  ? 'granted' : 'denied', 
                'functionality_storage': cookie.categories.includes('necessary')  ? 'granted' : 'denied', 
                'personalization_storage': cookie.categories.includes('necessary')  ? 'granted' : 'denied', 
                'security_storage': 'granted', 
            }); 
        }, 
 
 
        onChange: ({ cookie, changedCategories, changedServices }) => { 
            console.log(cookie,  changedCategories, changedServices); 
            // 当用户更改选择时，更新本地存储中的选择结果 
            localStorage.setItem('cookieConsent',  JSON.stringify(cookie));  
            gtag('consent', 'update', { 
                'ad_storage': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'ad_user_data': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'ad_personalization': cookie.categories.includes('marketing')  ? 'granted' : 'denied', 
                'analytics_storage': cookie.categories.includes('analytics')  ? 'granted' : 'denied', 
                'functionality_storage': cookie.categories.includes('necessary')  ? 'granted' : 'denied', 
                'personalization_storage': cookie.categories.includes('necessary')  ? 'granted' : 'denied', 
                'security_storage': 'granted', 
            }); 
        } 
    }); 
} else { 
    // 如果本地存储中已经有选择结果，直接使用该结果更新 Google Analytics 的同意状态 
    const savedConsent = JSON.parse(localStorage.getItem('cookieConsent'));  
    gtag('consent', 'update', { 
        'ad_storage': savedConsent.categories.includes('marketing')  ? 'granted' : 'denied', 
        'ad_user_data': savedConsent.categories.includes('marketing')  ? 'granted' : 'denied', 
        'ad_personalization': savedConsent.categories.includes('marketing')  ? 'granted' : 'denied', 
        'analytics_storage': savedConsent.categories.includes('analytics')  ? 'granted' : 'denied', 
        'functionality_storage': savedConsent.categories.includes('necessary')  ? 'granted' : 'denied', 
        'personalization_storage': savedConsent.categories.includes('necessary')  ? 'granted' : 'denied', 
        'security_storage': 'granted', 
    }); 
} 
 
