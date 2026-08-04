# E069FAS

## Descrição

Tabelas - Seguros - Faixas de aplicação do seguro

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodGps | String(015) | Não | Código do Grupo de Produto/Serviço |
| VlrIni | Number(015,2) | Não | Valor inicial da faixa |
| VlrFim | Number(015,2) | Não | Valor final da faixa |
| PerPre | Number(005,2) | Não | Percentual de prêmio com IOF |
| PerCom | Number(005,2) | Não | Percentual de comissão |
| IdeCse | Number(009,0) | Não | Idenficador do registro do cadastro do seguro |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E069FASIndice2

**Tipo:** Não unico

Campos:
- IdeCse

### E069FASIndice3

**Tipo:** Não unico

Campos:
- CodGps

---

## Relacionamentos

### IR_E069FAS_001

**Tabela:** E069GPS

| Origem | Destino |
|--------|---------|
| CodGps | CodGps |

### IR_E069FAS_006

**Tabela:** E069CSE

| Origem | Destino |
|--------|---------|
| IdeCse | IdeUni |

