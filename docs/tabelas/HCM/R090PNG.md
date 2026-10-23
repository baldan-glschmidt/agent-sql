# R090PNG

## Descrição

Cadastro de Pessoas Não Gratas

---

## Resumo

- Campos: 23
- Chave Primária: 2 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento da Pessoa Não Grata |
| NumDoc | String(020) | Não | Número do Documento da Pessoa Não Grata |
| NomPng | String(040) | Sim | Nome |
| ApePng | String(050) | Sim | Apelido |
| NomPai | String(040) | Sim | Nome do Pai |
| NomMae | String(070) | Sim | Nome da Mãe |
| DocOri | String(020) | Sim | Documento de Origem |
| DatNas | Date | Sim | Data de Nascimento |
| VinPng | String(001) | Sim | Vínculo |
| SegTDo | Number(001,0) | Sim | Segundo Tipo do Documento do Visitante |
| SegDoc | String(020) | Sim | Segundo Número do Documento do Visitante |
| ProPng | String(1000) | Sim | Procedimento a Realizar |
| PerEnt | String(001) | Sim | Permite Entrada |
| MotPng | String(120) | Sim | Motivo |
| FotPng | Image | Sim | Foto |
| CodMot | Number(002,0) | Sim | Código do Motivo |
| DatCad | Date | Sim | Data de Inclusão no Cadastro |
| NumEmp | Number(004,0) | Sim | Código da Empresa de Origem |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro de Origem na Ficha Básica |
| BloHom | String(001) | Sim | Bloqueia o Registro qdo for Homônimo |
| PerHom | String(001) | Sim | Permite Entrada Homônimo |
| CodUsu | Number(010,0) | Sim | Código do usuário que cadastrou o documento |

---

## Chave Primária

- TipDoc
- NumDoc

---

## Índices

### R090PNGIndice2

**Tipo:** Não unico

Campos:
- NomPng

### R090PNGIndice3

**Tipo:** Não unico

Campos:
- ApePng

### R090PNGIndice4

**Tipo:** Não unico

Campos:
- SegTDo
- SegDoc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
