%global package_speccommit 8e5aaf54f1feb9883331716a6576a5d1eca823c4
%global usver 4.2
%global xsver 5
%global xsrel %{xsver}%{?xscount}%{?xshash}
Name:        mdadm
Version:     4.2
Release:     %{?xsrel}%{?dist}
Summary:     The mdadm program controls Linux md devices (software RAID arrays)
URL:         http://www.kernel.org/pub/linux/utils/raid/mdadm/
License:     GPLv2+

Source0: mdadm-4.2.tar.xz
Source1: raid-check
Source2: mdadm-raid-check-sysconfig
Source3: mdmonitor.service
Source4: mdadm.conf
Source5: mdadm_event.conf
Source6: raid-check.timer
Source7: raid-check.service
Source8: mdcheck
Patch0: 0001-Unify-error-message.patch
Patch1: 0002-mdadm-Fix-double-free.patch
Patch2: 0003-Grow_reshape-Add-r0-grow-size-error-message-and-upda.patch
Patch3: 0004-udev-adapt-rules-to-systemd-v247.patch
Patch4: 0005-Replace-error-prone-signal-with-sigaction.patch
Patch5: 0006-mdadm-Respect-config-file-location-in-man.patch
Patch6: 0007-mdadm-Update-ReadMe.patch
Patch7: 0008-mdadm-Update-config-man-regarding-default-files-and-.patch
Patch8: 0009-mdadm-Update-config-manual.patch
Patch9: 0010-Create-Build-use-default_layout.patch
Patch10: 0011-mdadm-add-map_num_s.patch
Patch11: 0012-mdadm-systemd-remove-KillMode-none-from-service-file.patch
Patch12: 0013-mdmon-Stop-parsing-duplicate-options.patch
Patch13: 0014-Grow-block-n-on-external-volumes.patch
Patch14: 0015-Incremental-Fix-possible-memory-and-resource-leaks.patch
Patch15: 0016-Mdmonitor-Fix-segfault.patch
Patch16: 0017-Mdmonitor-Improve-logging-method.patch
Patch17: 0018-Fix-possible-NULL-ptr-dereferences-and-memory-leaks.patch
Patch18: 0019-imsm-Remove-possibility-for-get_imsm_dev-to-return-N.patch
Patch19: 0020-Revert-mdadm-fix-coredump-of-mdadm-monitor-r.patch
Patch20: 0021-util-replace-ioctl-use-with-function.patch
Patch21: 0022-mdadm-super1-restore-commit-45a87c2f31335-to-fix-clu.patch
Patch22: 0023-imsm-introduce-get_disk_slot_in_dev.patch
Patch23: 0024-imsm-use-same-slot-across-container.patch
Patch24: 0025-imsm-block-changing-slots-during-creation.patch
Patch25: 0026-mdadm-block-update-ppl-for-non-raid456-levels.patch
Patch26: 0027-mdadm-Fix-array-size-mismatch-after-grow.patch
Patch27: 0028-mdadm-Remove-dead-code-in-imsm_fix_size_mismatch.patch
Patch28: 0029-Monitor-use-devname-as-char-array-instead-of-pointer.patch
Patch29: 0030-Monitor-use-snprintf-to-fill-device-name.patch
Patch30: 0031-Makefile-Don-t-build-static-build-with-everything-an.patch
Patch31: 0032-DDF-Cleanup-validate_geometry_ddf_container.patch
Patch32: 0033-DDF-Fix-NULL-pointer-dereference-in-validate_geometr.patch
Patch33: 0034-mdadm-Grow-Fix-use-after-close-bug-by-closing-after-.patch
Patch34: 0035-monitor-Avoid-segfault-when-calling-NULL-get_bad_blo.patch
Patch35: 0036-mdadm-Fix-mdadm-r-remove-option-regression.patch
Patch36: 0037-mdadm-Fix-optional-write-behind-parameter.patch
Patch37: 0038-tests-00raid0-add-a-test-that-validates-raid0-with-l.patch
Patch38: 0039-tests-fix-raid0-tests-for-0.90-metadata.patch
Patch39: 0040-tests-04update-metadata-avoid-passing-chunk-size-to-.patch
Patch40: 0041-tests-02lineargrow-clear-the-superblock-at-every-ite.patch
Patch41: 0042-mdadm-test-Add-a-mode-to-repeat-specified-tests.patch
Patch42: 0043-mdadm-test-Mark-and-ignore-broken-test-failures.patch
Patch43: 0044-tests-Add-broken-files-for-all-broken-tests.patch
Patch44: 0045-mdadm-Replace-obsolete-usleep-with-nanosleep.patch
Patch45: 0046-tests-00readonly-Run-udevadm-settle-before-setting-r.patch
Patch46: 0047-tests-add-test-for-names.patch
Patch47: 0048-mdadm-remove-symlink-option.patch
Patch48: 0049-mdadm-move-data_offset-to-struct-shape.patch
Patch49: 0050-mdadm-Don-t-open-md-device-for-CREATE-and-ASSEMBLE.patch
Patch50: 0051-Grow-Split-Grow_reshape-into-helper-function.patch
Patch51: 0052-Assemble-check-if-device-is-container-before-schedul.patch
Patch52: 0053-super1-report-truncated-device.patch
Patch53: 0054-mdadm-Correct-typos-punctuation-and-grammar-in-man.patch
Patch54: 0055-Manage-Block-unsafe-member-failing.patch
Patch55: 0056-Monitor-Fix-statelist-memory-leaks.patch
Patch56: 0057-mdadm-added-support-for-Intel-Alderlake-RST-on-VMD-p.patch
Patch57: 0058-mdadm-Add-Documentation-entries-to-systemd-services.patch
Patch58: 0059-ReadMe-fix-command-line-help.patch
Patch59: 0060-mdadm-replace-container-level-checking-with-inline.patch
Patch60: 0061-Mdmonitor-Omit-non-md-devices.patch
Patch61: 0062-Mdmonitor-Split-alert-into-separate-functions.patch
Patch62: 0063-Monitor-block-if-monitor-modes-are-combined.patch
Patch63: 0064-Update-mdadm-Monitor-manual.patch
Patch64: 0065-Grow-fix-possible-memory-leak.patch
Patch65: 0066-mdadm-create-ident_init.patch
Patch66: 0067-mdadm-Add-option-validation-for-update-subarray.patch
Patch67: 0068-Fix-update-subarray-on-active-volume.patch
Patch68: 0069-Add-code-specific-update-options-to-enum.patch
Patch69: 0070-super-ddf-Remove-update_super_ddf.patch
Patch70: 0071-super0-refactor-the-code-for-enum.patch
Patch71: 0072-super1-refactor-the-code-for-enum.patch
Patch72: 0073-super-intel-refactor-the-code-for-enum.patch
Patch73: 0074-Change-update-to-enum-in-update_super-and-update_sub.patch
Patch74: 0075-Manage-Incremental-code-refactor-string-to-enum.patch
Patch75: 0076-Change-char-to-enum-in-context-update-refactor-code.patch
Patch76: 0077-mdmon-fix-segfault.patch
Patch77: 0078-util-remove-obsolete-code-from-get_md_name.patch
Patch78: 0079-mdadm-udev-Don-t-handle-change-event-on-raw-devices.patch
Patch79: 0080-Manage-do-not-check-array-state-when-drive-is-remove.patch
Patch80: 0081-incremental-manage-do-not-verify-if-remove-is-safe.patch
Patch81: 0082-super-intel-make-freesize-not-required-for-chunk-siz.patch
Patch82: 0083-manage-move-comment-with-function-description.patch
Patch83: 0084-Revert-mdadm-systemd-remove-KillMode-none-from-servi.patch
Patch84: 0085-Grow-fix-can-t-change-bitmap-type-from-none-to-clust.patch
Patch85: 0086-Fix-NULL-dereference-in-super_by_fd.patch
Patch86: 0087-Mdmonitor-Make-alert_info-global.patch
Patch87: 0088-Mdmonitor-Pass-events-to-alert-using-enums-instead-o.patch
Patch88: 0089-Mdmonitor-Add-helper-functions.patch
Patch89: 0090-Add-helpers-to-determine-whether-directories-or-file.patch
Patch90: 0091-Mdmonitor-Refactor-write_autorebuild_pid.patch
Patch91: 0092-Mdmonitor-Refactor-check_one_sharer-for-better-error.patch
Patch92: 0093-util.c-reorder-code-lines-in-parse_layout_faulty.patch
Patch93: 0094-util.c-fix-memleak-in-parse_layout_faulty.patch
Patch94: 0095-Detail.c-fix-memleak-in-Detail.patch
Patch95: 0096-isuper-intel.c-fix-double-free-in-load_imsm_mpb.patch
Patch96: 0097-super-intel.c-fix-memleak-in-find_disk_attached_hba.patch
Patch97: 0098-super-ddf.c-fix-memleak-in-get_vd_num_of_subarray.patch
Patch98: 0099-Create-goto-abort_locked-instead-of-return-1-in-erro.patch
Patch99: 0100-Create-remove-safe_mode_delay-local-variable.patch
Patch100: 0101-Create-Factor-out-add_disks-helpers.patch
Patch101: 0102-mdadm-Introduce-pr_info.patch
Patch102: 0103-mdadm-Add-write-zeros-option-for-Create.patch
Patch103: 0104-tests-00raid5-zero-Introduce-test-to-exercise-write-.patch
Patch104: 0105-manpage-Add-write-zeroes-option-to-manpage.patch
Patch105: 0106-Define-alignof-using-_Alignof-when-using-C11-or-newe.patch
Patch106: 0107-Use-existence-of-etc-initrd-release-to-detect-initrd.patch
Patch107: 0108-mdmon-don-t-test-both-all-and-container_name.patch
Patch108: 0109-mdmon-change-systemd-unit-file-to-use-foreground.patch
Patch109: 0110-mdmon-Remove-need-for-KillMode-none.patch
Patch110: 0111-mdmon-Improve-switchroot-interactions.patch
Patch111: 0112-mdopen-always-try-create_named_array.patch
Patch112: 0113-Improvements-for-IMSM_NO_PLATFORM-testing.patch
Patch113: 0114-Revert-Revert-mdadm-systemd-remove-KillMode-none-fro.patch
Patch114: 0115-Create-Fix-checking-for-container-in-update_metadata.patch
Patch115: 0116-Fix-null-pointer-for-incremental-in-mdadm.patch
Patch116: 0117-super1-fix-truncation-check-for-journal-device.patch
Patch117: 0118-Fix-some-cases-eyesore-formatting.patch
Patch118: 0119-Bump-minimum-kernel-version-to-2.6.32.patch
Patch119: 0120-Remove-the-config-files-in-mdcheck_start-continue-se.patch
Patch120: mdadm-udev.patch
Patch121: mdadm-2.5.2-static.patch
Patch122: disable-Werror.patch

BuildRequires: make
BuildRequires: systemd-units binutils-devel gcc systemd-devel
Requires(post): systemd-units coreutils
Requires(preun): systemd-units
Requires(postun): systemd-units coreutils

%description
The mdadm program is used to create, manage, and monitor Linux MD (software
RAID) devices.  As such, it provides similar functionality to the raidtools
package.  However, mdadm is a single program, and it can perform
almost all functions without a configuration file, though a configuration
file can be used to help with some common tasks.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} CXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" SYSCONFDIR="%{_sysconfdir}" mdadm mdmon

%install
make DESTDIR=%{buildroot} MANDIR=%{_mandir} BINDIR=%{_sbindir} SYSTEMD_DIR=%{_unitdir} UDEVDIR=/usr/lib/udev/ install install-systemd
install -Dp -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/raid-check
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/raid-check
mkdir -p -m 710 %{buildroot}/run/mdadm
mkdir -p -m 700 %{buildroot}/usr/share/mdadm
install -Dp -m 755 %{SOURCE8} %{buildroot}/usr/share/mdadm/mdcheck

# systemd
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE3} %{buildroot}%{_unitdir}
install -m644 %{SOURCE6} %{buildroot}%{_unitdir}
install -m644 %{SOURCE7} %{buildroot}%{_unitdir}

# tmpfile
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0710 %{buildroot}/run/%{name}/

%post
%systemd_post mdmonitor.service raid-check.timer
%{_bindir}/systemctl disable mdmonitor-takeover.service  >/dev/null 2>&1 || :

%preun
%systemd_preun mdmonitor.service raid-check.timer

%postun
%systemd_postun_with_restart mdmonitor.service

%files
%license COPYING
%doc mdadm.conf-example misc/*
%{_udevrulesdir}/*
%{_sbindir}/*
%{_unitdir}/*
%{_mandir}/man*/md*
/usr/lib/systemd/system-shutdown/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%dir /run/%{name}/
%config(noreplace) %{_tmpfilesdir}/%{name}.conf
/usr/share/mdadm/mdcheck

%changelog
* Thu Jun 19 2025 Gerald Elder-Vass <gerald.elder-vass@cloud.com> - 4.2-5
- Disable rpmlint hardcoded path checks

* Wed Jun 18 2025 Gerald Elder-Vass <gerald.elder-vass@cloud.com> - 4.2-4
- CA-412437: mdadm-4.2-4 for XS8 and mdp fixes

* Thu Aug 15 2024 Stephen Cheng <stephen.cheng@cloud.com> - 4.2-3
- CP-46115: Remove libreport-filesystem dependency

* Tue Jan 02 2024 Fei Su <fei.su@cloud.com> - 4.2-2
- Update to latest upstream

* Mon Sep 18 2023 Qin Zhang <qin.zhang@citrix.com> - 4.2-1
- First imported release

