# R999PSF

## Descrição

Configuração da Tela de Pesquisa de Registros - Campos

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomPsq | String(035) | Não | Nome da consulta, normalmente será o nome da tabela |
| CodUsu | Number(010,0) | Não | Código do usuário |
| SrcFrm | String(030) | Não | Nome do form origem |
| FldNam | String(050) | Não | Nome do Campo |
| Width | Number(005,0) | Sim | Largura do campo na tela |
| IndexF | Number(005,0) | Sim | Posição do campo na tela |
| KidOrd | Number(005,0) | Sim | Tipo de ordenação do campo (ascendente ou descendente) |

---

## Chave Primária

- NomPsq
- CodUsu
- SrcFrm
- FldNam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R999PSF_002

**Tabela:** R999PSQ

| Origem | Destino |
|--------|---------|
| NomPsq | NomPsq |
| CodUsu | CodUsu |
| SrcFrm | SrcFrm |

