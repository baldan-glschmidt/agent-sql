# R304ACA

## Descrição

e-Sfinge Online - Arquivos da Concessão Aposentadoria

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumAto | String(016) | Não | Número do ato de pessoal |
| DatAto | Date | Não | Data do ato de pessoal |
| NumMat | String(016) | Não | Número da matrícula do servidor na unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na receita federal |
| CodUni | Number(016,0) | Não | Código da unidade gestora do servidor |
| NomArq | String(255) | Não | Nome do arquivo |
| TipDoc | Number(003,0) | Não | Tipo do documento |
| SeqReg | Number(009,0) | Não | Sequência |
| UrlArq | String(1000) | Sim | URL do arquivo (se disponível online) |
| ArqDoc | Image | Sim | Arquivo do documento |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumAto
- DatAto
- NumMat
- NumCpf
- CodUni
- NomArq
- TipDoc
- SeqReg

---

## Índices

### R304ACAIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
