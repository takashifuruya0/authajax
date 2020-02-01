import rules
import guardian


@rules.predicate
def is_article_owner(user, article):
    return article.created_by == user


# @rules.predicate
# def has_model_level_permission(user):
#     return user.has_perm('web.read_article')


@rules.predicate
def is_article_pro(user, article):
    print("user.is_pro {}".format(user.is_pro))
    print("article.is_for_pro {}".format(article.is_for_pro))
    if (user.is_pro and article.is_for_pro) or not article.is_for_pro:
        return True
    else:
        return False
    # return True


rules.add_perm('web.rules_read_article', is_article_pro)
rules.add_perm('web.rules_update_article', is_article_owner & is_article_pro)
rules.add_perm('web.rules_delete_article', is_article_owner)
