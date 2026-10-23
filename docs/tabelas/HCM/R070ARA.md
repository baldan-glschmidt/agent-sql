# R070ARA

## Descrição

Marcações de acesso em recinto alfandegado

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(017,0) | Não | Código sequencial |
| CodPlt | Number(005,0) | Não | Código do Site |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatAcc | Date | Sim | Data do Acesso |
| HorAcc | Number(005,0) | Sim | Hora do Acesso |
| SeqAcc | Number(002,0) | Sim | Sequência do Registro |
| DirAcc | String(001) | Sim | Direção do Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| IdtPes | String(023) | Sim | Identificador da Pessoa |
| NomPes | String(040) | Sim | Nome |
| TipDoc | Number(001,0) | Sim | Tipo do documento |
| NumDoc | String(020) | Sim | Número do documento |
| PlaVei | String(010) | Sim | Placa do Veículo |
| NumRen | String(011) | Sim | Código Renavam (Documento do Veículo) |
| CraVei | Number(012,0) | Sim | Número do crachá do veículo |
| TipMar | String(001) | Sim | Tipo da Marcação |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| IdeAcc | String(002) | Sim | Tipo de identificação usado no controle de acesso |
| CPFRes | String(020) | Sim | CPF do reponsável pelo registro da ocorrência |

---

## Chave Primária

- SeqReg
- CodPlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
