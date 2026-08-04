# E027BNF

## Descrição

Tabelas - Situações Tributárias X Dispositivo Fiscal

---

## Resumo

- Campos: 20
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SigUfs | String(002) | Não | Sigla do estado |
| CodStr | String(003) | Não | Código da Situação Tributária ICMS |
| DatIni | Date | Não | Data de início da vigência |
| CodClf | String(003) | Não | Código da classificação fiscal |
| CodTns | String(005) | Não | Código da transação |
| CodPro | String(014) | Não | Código do produto |
| CodSer | String(014) | Não | Código do serviço |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| GerSbn | String(001) | Sim | Indicativo para gerar a literal 'SEM CBENEF' na NF-e |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodMs1 | Number(004,0) | Sim | Código da mensagem - 1 |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 |

---

## Chave Primária

- CodEmp
- SigUfs
- CodStr
- DatIni
- CodClf
- CodTns
- CodPro
- CodSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
