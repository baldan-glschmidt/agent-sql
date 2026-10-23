# R088DAE

## Descrição

Documentos anexos de veículos

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatReg | Date | Não | Data Registro |
| HorReg | Number(005,0) | Não | Hora Registro |
| TipDoc | Number(004,0) | Não | Código do Tipo de Documento |
| SeqDoc | Number(006,0) | Não | Sequência Documento |
| OriDoc | Number(001,0) | Sim | Origem do Documento |
| NomArq | String(250) | Sim | Nome do Arquivo anexo |
| DocAne | Image | Sim | Documento anexo |
| ObsDoc | String(700) | Sim | Observação do Documento |

---

## Chave Primária

- PlaVei
- DatReg
- HorReg
- TipDoc
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
