# R058DIE

## Descrição

Driver Informações Extensíveis

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDrv | Number(003,0) | Não | Código de Cadastro do Driver Integrador |
| IdtIed | String(020) | Não | Identificador Informação Extensível do Driver |
| TieDrv | Number(001,0) | Sim | Tipo Informação Extensível |
| InfExt | String(512) | Sim | Dado Informação Extensível |

---

## Chave Primária

- CodDrv
- IdtIed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058DIE_000

**Tabela:** R058DRV

| Origem | Destino |
|--------|---------|
| CodDrv | CodDrv |

