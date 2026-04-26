# GitLab Setup Guide (Recommended)

I cannot directly change your GitLab project settings from this local coding environment,
but here is the exact click-path to configure the important ones.

## 1) Protect the `main` branch

1. Open your GitLab project.
2. Go to **Settings → Repository**.
3. Expand **Protected branches**.
4. In **Branch**, select `main`.
5. Set:
   - **Allowed to merge**: Maintainers (or your preferred role)
   - **Allowed to push**: No one (or Maintainers only)
6. Click **Protect**.

## 2) Require Merge Requests + approvals

1. Go to **Settings → Merge requests**.
2. Enable:
   - **Pipelines must succeed**
   - **All discussions must be resolved**
3. Go to **Settings → General → Merge request approvals** (or **Settings → Merge requests → Approvals**, depending on GitLab version).
4. Set required approvers (e.g., 1).

## 3) Require CI before merge

1. Confirm `.gitlab-ci.yml` is on default branch.
2. In **Settings → Merge requests**, ensure **Pipelines must succeed** is enabled.
3. (Optional) Enable **Only allow merge if all status checks pass** if your tier provides it.

## 4) Add labels and milestones for learning flow

### Labels
Go to **Issues → Labels** and create:
- `learning`
- `feature`
- `bug`
- `refactor`
- `docs`

### Milestones
Go to **Issues → Milestones** and create examples like:
- `M1 - Game Loop Fundamentals`
- `M2 - Input + Movement`
- `M3 - Collision + States`

## 5) Add a Merge Request template

1. Create folder: `.gitlab/merge_request_templates/`
2. Add file: `default.md`
3. Suggested template:

```md
## Summary
- 

## Why
- 

## Testing
- [ ] Local tests pass
- [ ] CI passes

## Notes
- 
```

## 6) Optional quality/security additions

If you want, next steps can include:
- Ruff/Black checks in CI
- Pytest job in CI
- GitLab SAST template include (tier-dependent)

---

If you want, I can also generate a hardened `.gitlab-ci.yml` next with lint + format + test stages.
