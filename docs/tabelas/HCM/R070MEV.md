# R070MEV

## Descrição

Monitoramento de Evacuação

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatIns | Date | Não | Data de Inserção |
| HorIns | Number(005,0) | Não | Hora de Inserção |
| SeqIns | Number(004,0) | Não | Sequência de Inserção |
| TpOper | Number(001,0) | Não | Tipo de Operação |
| IdtPes | String(023) | Não | Identificador da Pessoa |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| DatAcc | Date | Sim | Data do Acesso |
| HorAcc | Number(005,0) | Sim | Hora do Acesso |
| CodUsu | Number(009,0) | Sim | Código do Usuário |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- DatIns
- HorIns
- SeqIns
- TpOper
- IdtPes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
