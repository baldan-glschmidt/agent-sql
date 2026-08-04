# E049DEC

## Descrição

Tabelas - Declarações

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDec | Number(009,0) | Não | Código da declaração |
| DesDec | String(250) | Não | Descrição da declaração |
| ModDec | String(003) | Não | Módulo de aplicação da declaração |
| VerDec | Number(005,2) | Sim | Versão da declaração |
| ObsDec | String(250) | Sim | Observação da declaração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| SitDec | String(001) | Não | Situação do cadastro da declaração |
| TipDec | String(001) | Sim | Tipo do leiaute da declaração |
| DelCam | String(001) | Sim | Caracter delimitador do registro |
| SisDec | Number(002,0) | Não | Identificará o Tipo de Sistema de uma determinada declaração |
| TipArq | String(001) | Sim | Tipo de arquivo gerado |

---

## Chave Primária

- CodDec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
