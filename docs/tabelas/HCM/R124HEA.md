# R124HEA

## Descrição

Colaborador - Emprego Anterior

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
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| DatAdm | Date | Sim | Data de Admissão |
| CodOem | Number(008,0) | Sim | Empresa Anterior |
| NomOem | String(060) | Sim | Nome da empresa |
| DatDem | Date | Sim | Data de Demissão |
| MotDem | Number(003,0) | Sim | Motivo da Demissão |
| UltSal | Number(011,2) | Sim | Último Salário |
| DesMoe | String(005) | Sim | Símbolo Moeda |
| TemSer | Number(005,0) | Sim | Tempo de Serviço no Emprego Anterior, em meses |
| ComEmp | String(1000) | Sim | Comentário do Emprego |
| CodAtu | Number(005,0) | Sim | Código do ramo de atuação da empresa |
| DesAtu | String(060) | Sim | Descrição do ramo de atuação da empresa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAdm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
