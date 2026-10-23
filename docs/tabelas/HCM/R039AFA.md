# R039AFA

## Descrição

Afastamentos Retroativos eSocial

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAfa | Date | Não | Data do Afastamento |
| DatTer | Date | Sim | Data do Término do Afastamento |
| ObsAfa | String(255) | Sim | Observação do Afastamento |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| NomAte | String(070) | Sim | Nome do Atendente |
| OrgCla | Number(001,0) | Sim | Órgão de Classe |
| RegCon | String(014) | Sim | Registro no Conselho Profissional |
| EstCon | String(002) | Sim | UF do Conselho Profissional |
| AciTra | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAfa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
