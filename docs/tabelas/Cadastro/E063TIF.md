# E063TIF

## Descrição

Tabelas - Vínculo - Ticket de Pesagem x Fotos.

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatEnt | Date | Não | Data da entrada |
| SeqEnt | Number(006,0) | Não | Sequência de entrada  na data |
| IdePca | Number(014,0) | Não | Identificador do Processo de Captura das Fotos da Pesagem |
| SeqFot | Number(004,0) | Não | Sequência da Foto |
| OpeBal | Number(001,0) | Não | Operação da Balança |
| FinCam | Number(001,0) | Não | Finalidade da Câmera |
| ForCap | Number(001,0) | Sim | Forma de Captura |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- IdePca
- SeqFot
- DatEnt
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
