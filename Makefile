HOME=$(shell pwd)
VERSION="3.1.1"
RELEASE="1"

all: build

clean:
	rm -rf ./rpmbuild
	mkdir -p ./rpmbuild/SPECS/ ./rpmbuild/SOURCES/
	mkdir -p ./SPECS ./SOURCES

download-upstream:
	./download kibana-${VERSION}.tar.gz https://download.elasticsearch.org/kibana/kibana/kibana-${VERSION}.tar.gz

build: clean download-upstream
	cp -r ./SPECS/* ./rpmbuild/SPECS/ || true
	cp -r ./SOURCES/* ./rpmbuild/SOURCES/ || true
	rpmbuild -ba SPECS/kibana.spec \
	--define "ver ${VERSION}" \
	--define "rel ${RELEASE}" \
	--define "_topdir %(pwd)/rpmbuild" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
