# R108RNA

## Descrição

Registro de Notificação Compulsória - Atendimentos - Anexos

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAte | Date | Não | Data do Atendimento |
| HorAte | Number(005,0) | Não | Hora do Atendimento |
| SeqArq | Number(003,0) | Não | Sequência do arquivo |
| NomArq | String(250) | Sim | Nome do arquivo de anexo |
| DesArq | String(060) | Sim | Descrição do anexo |
| ArqAne | Image | Sim | Anexo |

---

## Chave Primária

- NumEmp
- CodFic
- DatAte
- HorAte
- SeqArq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
