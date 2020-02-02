import rules
import guardian


@rules.predicate
def is_article_owner(user, article):
    return article.created_by == user


@rules.predicate
def is_article_pro_or_free(user, article):
    if (user.is_pro and article.is_for_pro) or not article.is_for_pro:
        return True
    else:
        return False


rules.add_perm('web.rules_read_article', is_article_pro_or_free)
rules.add_perm('web.rules_update_article', is_article_owner)
rules.add_perm('web.rules_delete_article', is_article_owner)
