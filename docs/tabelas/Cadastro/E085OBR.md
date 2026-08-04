# E085OBR

## Descrição

Obras Relacionadas ao Cliente/Imóvel

---

## Resumo

- Campos: 21
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CODCLI | Number(009,0) | Não | Código do Cliente |
| CODOBR | String(020) | Não | Código da obra |
| IMOCLI | String(020) | Sim | Código do imóvel |
| IniObr | Date | Sim | Data do Início da Obra |
| FimObr | Date | Sim | Data do Fim da Obra |
| InsImf | String(020) | Sim | Inscrição imobiliária |
| DesImo | String(250) | Não | Descrição resumida sobre as informações relevantes a Obra |
| CodCib | String(020) | Sim | Código CIB |
| NumCno | String(020) | Sim | Número CNO |
| TipLog | String(050) | Sim | Tipo de logradouro |
| NomLog | String(100) | Sim | Nome do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| Complo | String(050) | Sim | Complemento do endereço |
| Bairro | String(050) | Sim | Bairro |
| SigUfs | String(002) | Sim | Sigla da unidade federativa |
| CepNac | Number(008,0) | Sim | CEP Nacional |
| CidNac | String(050) | Sim | Cidade nacional |
| CodPai | String(005) | Sim | Código do país |
| CepExt | String(020) | Sim | CEP exterior |
| CidExt | String(050) | Sim | Cidade exterior |
| EstExt | String(050) | Sim | Estado exterior |

---

## Chave Primária

- CODCLI
- CODOBR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
