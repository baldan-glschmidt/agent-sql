# R583GHE

## Descrição

GHE - Cadastro de GHE

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| DesGHE | String(200) | Sim | Descrição do GHE |
| DatCri | Date | Sim | Data de Criação do GHE |
| DatExt | Date | Sim | Data de Extinção do GHE |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico do GHE |
| AnoGHE | String(2000) | Sim | Anotações do GHE |

---

## Chave Primária

- CodPRA
- CodGHE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583GHE_000

**Tabela:** R583CAD

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |

