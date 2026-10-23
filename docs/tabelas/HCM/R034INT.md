# R034INT

## Descrição

Convocação Intermitente

---

## Resumo

- Campos: 27
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCon | Number(015,0) | Não | Código da Convocação |
| DatCon | Date | Sim | Data da Convocação |
| HorCon | Number(005,0) | Sim | Hora da Convocação |
| DatIni | Date | Sim | Data Início da Convocação |
| DatFim | Date | Sim | Data Fim da Convocação |
| DatPgt | Date | Sim | Data Prevista para Pagamento |
| DesJor | String(999) | Sim | Descrição da Jornada |
| IntCon | String(080) | Sim | Instrumento utilizado para a convocação |
| IndLoc | Number(001,0) | Sim | Indidicativo do local de trabalho |
| EndCep | Number(008,0) | Sim | CEP |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| DesLog | String(080) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado |
| CodCid | Number(007,0) | Sim | Cidade |
| CodBai | Number(004,0) | Sim | Bairro |
| IndSta | Number(001,0) | Sim | Status da Convocação |
| DatSta | Date | Sim | Data do aceite/recusa |
| HorSta | Number(005,0) | Sim | Hora do aceite/recusa |
| IntSta | String(080) | Sim | Instrumento utilizado para o retorno |
| DesSta | String(999) | Sim | Descrição da Recusa |
| CodCal | Number(005,0) | Sim | Código de Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
