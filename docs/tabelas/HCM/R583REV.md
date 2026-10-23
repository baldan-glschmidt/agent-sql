# R583REV

## Descrição

GHE - Revisão do GHE

---

## Resumo

- Campos: 21
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| DesRev | String(060) | Sim | Descrição da revisão do GHE |
| DatIni | Date | Sim | Data de início da Revisão do GHE |
| DatTer | Date | Sim | Data de término da Revisão do GHE |
| RevPRA | String(010) | Sim | Indica a qual revisão de PGR esta revisão pertence |
| DesAri | String(8000) | Sim | Descrição do Ambiente de Risco |
| ConAmb | String(3000) | Sim | Condições ambientais de trabalho |
| SitEso | Number(001,0) | Sim | Situação para envio ao eSocial |
| AtiRis | String(8000) | Sim | Descrição das Atividades de Risco do GHE |
| MedPro | String(001) | Sim | Medidas de proteção (Obsoleto) |
| ConFun | String(001) | Sim | Condições de funcionamento (Obsoleto) |
| PraVal | String(001) | Sim | Prazo de validade (Obsoleto) |
| PerTro | String(001) | Sim | Periocidade de troca (Obsoleto) |
| ObsHig | String(001) | Sim | Higienização (Obsoleto) |
| IntOrd | String(8001) | Sim | Uso na emissão da OS (Introdução) |
| OriOrd | String(8001) | Sim | Uso na emissão da OS (Orientação de Segurança do Trabalho) |
| ProOrd | String(8001) | Sim | Uso na emissão da OS (Procedimentos em caso de Acidente de Trabalho) |
| TrmOrd | String(8001) | Sim | Uso na emissão da OS (Termo de Responsabilidade) |
| NumAmb | Number(007,0) | Sim | Código do Ambiente de Trabalho |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583REV_001

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

### IR_R583REV_006

**Tabela:** R583RCP

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| RevPRA | RevPRA |

