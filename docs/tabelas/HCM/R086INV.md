# R086INV

## Descrição

Investigação Ocorrência

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| CodInv | Number(006,0) | Não | Código da Investigação |
| OcoAct | Number(006,0) | Sim | Código da Ocorrência (Incidente ou Acidente) |
| TipAct | Number(001,0) | Sim | Tipo Colaborador |
| CadAct | Number(009,0) | Sim | Cadastro do Colaborador |
| DatAct | Date | Sim | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Sim | Hora Acidente de Trabalho |
| DatIni | Date | Sim | Data de Início da Investigação |
| DatTer | Date | Sim | Data de Término da Investigação |
| SitInv | Number(001,0) | Sim | Situação da Investigação |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Novo Local |
| NumLoc | Number(009,0) | Sim | Local da ocorrência no organograma |
| ConInv | String(1000) | Sim | Conclusão da Investigação |
| USU_AciTra | String(001) | Sim | Ocorreu na empresa? |
| USU_ProTom | String(1000) | Sim | Providências Tomadas |
| USU_DesRes | String(1000) | Sim | Descrição Resumida do Ocorrido/ Análise Técnica SESMT |
| USU_MotAci | Number(001,0) | Sim | Motivo do Acidente |

---

## Chave Primária

- NumEmp
- TipOco
- CodInv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
