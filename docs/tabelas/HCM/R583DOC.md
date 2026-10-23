# R583DOC

## Descrição

GHE - Revisão do GHE - Laudo - Documentos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| SeqDoc | Number(003,0) | Não | Sequência do Documento |
| DesDoc | String(050) | Sim | Descrição de identificação do documento |
| Imagem | Image | Sim | Documento |
| AnoDoc | String(700) | Sim | Anotações do Documento |
| NomArq | String(250) | Sim | Nome do Arquivo |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583DOC_002

**Tabela:** R583REV

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |

